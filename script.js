document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("product-form");
    const filterBtn = document.getElementById("filter-btn");
    const modal = document.getElementById("modal");
    const modalProductName = document.getElementById("modal-product-name");
    const modalQuantity = document.getElementById("modal-quantity");
    const modalPrice = document.getElementById("modal-price");
    const closeModal = document.querySelector(".close");
  
    const products = [];
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
  
      const name = document.getElementById("name").value;
      const category = document.getElementById("category").value;
      const description = document.getElementById("description").value;
      const price = parseFloat(document.getElementById("price").value);
      const quantity = parseInt(document.getElementById("quantity").value);
  
      products.push({
        name,
        category,
        description,
        price,
        quantity,
      });
  
      // Limpar o formulário após o cadastro
      form.reset();
    });
  
    filterBtn.addEventListener("click", function() {
      const filterName = document.getElementById("name").value;
      const filterCategory = document.getElementById("category").value;
  
      const filteredProducts = products.filter(product => {
        return (
          (!filterName || product.name.toLowerCase().includes(filterName.toLowerCase())) &&
          (!filterCategory || product.category.toLowerCase().includes(filterCategory.toLowerCase()))
        );
      });
  
      if (filteredProducts.length > 0) {
        modal.style.display = "block";
        modalProductName.textContent = filteredProducts[0].name;
        modalQuantity.textContent = filteredProducts[0].quantity;
        modalPrice.textContent = filteredProducts[0].price.toFixed(2);
      }
    });
  
    closeModal.addEventListener("click", function() {
      modal.style.display = "none";
    });
  
    window.addEventListener("click", function(event) {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    });
  });
  