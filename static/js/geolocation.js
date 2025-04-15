function sendLocationToSession(force = false) {
  if (force || !sessionStorage.getItem('locationSent')) {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        const data = {
          lat: position.coords.latitude,
          lon: position.coords.longitude
        };

        fetch('/save-location/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
          },
          body: JSON.stringify(data)
        }).then(() => {
          sessionStorage.setItem('locationSent', 'true');
          console.log('Location sent!');
        });
      });
    }
  }
}

// Helper: Get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Optional: Hook to a "refresh location" button
document.addEventListener('DOMContentLoaded', () => {
  const refreshBtn = document.getElementById('refresh-location-btn');
  if (refreshBtn) {
    refreshBtn.addEventListener('click', () => {
      sessionStorage.removeItem('locationSent');
      sendLocationToSession(true); // force update
    });
  }
});
