function fetchSuggestions(query) {
  fetch(`https://openlibrary.org/search.json?q=${encodeURIComponent(query)}&limit=7`)
    .then(response => response.json())
    .then(data => {
      const suggestions = data.docs.map(book => {
        const title = book.title || "No Title";
        const author = book.author_name ? book.author_name.join(", ") : "Unknown Author";
        const coverId = book.cover_i;
        const isbn = book.isbn && book.isbn.length > 0 ? book.isbn[0] : null;
        const coverUrl = coverId
          ? `https://covers.openlibrary.org/b/id/${coverId}-S.jpg`
          : "https://via.placeholder.com/50x75?text=No+Cover";

        if (!isbn) return '';  // skip if no ISBN

        return `
          <li class="list-group-item d-flex align-items-start">
          <a href="/contents/books/isbn/${isbn}/">
            <img src="${coverUrl}" alt="Cover" class="me-3" style="width:50px; height:75px; object-fit:cover;">
            <div>
              <div class="fw-bold">${title}</div>
              <small class="text-muted">${author}</small>
            </div>
            </a>
          </li>
        `;
      }).join("");


      document.getElementById("suggestions").innerHTML = suggestions.trim()
        ? `<ul class="list-group">${suggestions}</ul>`
        : `<li class="list-group-item text-muted">No results found.</li>`;
    })
    .catch(err => console.error("Error fetching suggestions:", err));
}

