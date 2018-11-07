export const getAll = () => {
    fetch("localhost:5000/api/v1/resources/all")
    .then(response => response.json)
}