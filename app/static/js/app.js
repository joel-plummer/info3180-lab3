/* Add your Application JavaScript */
addEventListener('DOMContentLoaded', () => {
  labels = document.querySelectorAll('form-control-label');
    labels.forEach(label => {
        label.style.color = 'red';
  });});