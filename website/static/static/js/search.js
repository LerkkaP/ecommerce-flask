document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.querySelector("#searchInput");
  const searchResults = document.getElementById("searchResults");

  searchInput.addEventListener("input", function () {
    const query = this.elements["search"].value;
    performSearch(query);
  });

  let currentSearch = null;

  function performSearch(query) {
    if (currentSearch) {
      currentSearch.abort();
    }

    currentSearch = new AbortController();
    const { signal } = currentSearch;

    if (query.trim() !== "") {
      fetch(`/search?search=${query}`, { signal })
        .then((response) => response.json())
        .then((data) => {
          if (data.watches.length > 0) {
            displayResults(data.watches);
            searchResults.style.display = "block";
          } else {
            displayNoResultsMessage();
          }
        })
        .catch((error) => {
          if (error.name !== "AbortError") {
            throw error;
          }
        });
    } else {
      searchResults.style.display = "none";
      searchResults.innerHTML = "";
    }
  }

  function displayNoResultsMessage() {
    const searchResults = document.querySelector(".search-results");
    searchResults.innerHTML = '<div class="no-results">No results found.</div>';
    searchResults.style.display = "block";
  }

  function displayResults(watches) {
    searchResults.innerHTML = "";
    for (const watch of watches) {
      const watchItem = document.createElement("div");
      watchItem.innerHTML = `
              <a href="/watch/${watch.id}">
                ${watch.brand} ${watch.model} ${watch.price} €
              </a>
            `;
      searchResults.appendChild(watchItem);
    }
  }

  searchInput.addEventListener("input", function () {
    const query = this.value;
    performSearch(query);
    positionResultsContainer();
  });

  function positionResultsContainer() {
    const inputRect = searchInput.getBoundingClientRect();
    searchResults.style.top = inputRect.bottom + "px";
    searchResults.style.left = inputRect.left + "px";
  }
});
