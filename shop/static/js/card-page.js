// Получаем форму для добавления в избранное
const addToFavoritesForm = document.querySelector('#add-to-favorites-form');

// Добавляем обработчик события отправки формы
addToFavoritesForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Предотвращаем отправку формы по умолчанию

  // Получаем URL-адрес для отправки AJAX-запроса из атрибута "action" формы
  const url = this.action;

  // Создаем новый экземпляр объекта FormData для сбора данных формы
  const formData = new FormData(this);

  // Отправляем AJAX-запрос на сервер
  fetch(url, {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      // Обработка успешного ответа сервера
      console.log(data.message); // Выводим сообщение в консоль
      // Можно выполнить дополнительные действия, например, обновить отображение на странице
    })
    .catch(error => {
      // Обработка ошибок
      console.error('Error:', error);
    });
});

