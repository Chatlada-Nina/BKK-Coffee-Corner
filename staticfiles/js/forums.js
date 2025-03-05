/* jshint esversion: 6 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated forum's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific forum.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let forumId = e.target.getAttribute("data-forum_id");
      deleteConfirm.href = `delete_forum/${forumId}`;
      deleteModal.show();
    });
  }