document.addEventListener("DOMContentLoaded", function () {
  if (document.querySelector("#edit_btn")) {
    document.querySelectorAll("#edit_btn").forEach(function (button) {
      button.onclick = function () {
        const csrftoken = document.querySelector(
          "[name=csrfmiddlewaretoken]"
        ).value;
        const postid = this.dataset.postid;
        const url = this.dataset.url;
        const ctt = document.querySelector("#ct" + postid);
        const orig = ctt.textContent.trim();

        // create a new textarea
        const textarea = document.createElement("textarea");
        textarea.value = orig;
        textarea.rows = 5;
        textarea.cols = 40;
        textarea.classList.add("edit-textarea");

        // create a new save button
        const save_btn = document.createElement("button");
        save_btn.textContent = "Save";
        save_btn.classList.add("save-btn");

        // replace the content with textarea
        ctt.replaceWith(textarea);

        // append the save button to the content
        textarea.after(save_btn);

        // hide the edit button
        this.style.display = "none";

        // the process after save button is cilcked
        save_btn.onclick = function () {
          const updated = textarea.value;

          fetch(url, {
            method: "POST",
            headers: {
              "X-CSRFToken": csrftoken,
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              updated: updated,
            }),
          })
            .then((response) => response.json())
            .then((data) => {
              console.log(data);
              if (data.success) {
                // Replace the textarea with the updated content paragraph
                const up_ctt = document.createElement("p");
                up_ctt.textContent = data.updated;
                up_ctt.id = "ct" + postid;
                up_ctt.classList.add("post-content");

                // replace the textarea with content
                textarea.replaceWith(up_ctt);
                save_btn.remove();

                button.style.display = "inline";
              } else {
                if (data.NOTMYSELF) {
                  alert(
                    "Server Rejected your request because you are not allowed to edit other's post!"
                  );
                } else if (data.EMPTY) {
                  alert(
                    "Server Rejected your request because the content is empty!"
                  );
                } else {
                  alert("Failed!");
                }
              }
            })
            .catch((error) => console.error("Error: ", error));
        };
      };
    });
  }
});
