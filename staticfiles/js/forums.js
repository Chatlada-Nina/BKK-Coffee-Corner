const editButtons = document.getElementsByClassName("btn-edit");
const forumText = document.getElementById("id_body");
const forumForm = document.getElementById("forumForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated forum's ID upon click.
* - Fetches the content of the corresponding forum.
* - Populates the `forumText` input/textarea with the forum's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_forum/{forumId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let forumId = e.target.getAttribute("forum_id");
    let forumContent = document.getElementById(`forum${forumId}`).innerText;
    forumText.value = forumContent;
    submitButton.innerText = "Update";
    forumForm.setAttribute("action", `edit_forum/${forumId}`);
  });
}

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
      let forumId = e.target.getAttribute("forum_id");
      deleteConfirm.href = `delete_forum/${forumId}`;
      deleteModal.show();
    });
  }