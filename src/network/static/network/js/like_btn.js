document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("#like_btn").forEach(function (button) {
    button.onclick = function () {
      const ID = this.dataset.postid;
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      const url = this.dataset.url;

      fetch(url, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          postid: ID,
        }),
      })
        .catch((error) => {
          console.log("Error: ", error);
        })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTP error! status: ${response.status}");
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);
          if (data.success) {
            var num = document.querySelector("#n_like" + ID);

            if (data.liked) {
              num.innerHTML = "💔 " + data.n_liker;
            } else {
              num.innerHTML = "❤️ " + data.n_liker;
            }
          } else {
            alert("Action Failed!");
          }
        })
        .catch((error) => {
          console.log("Error: ", error);
        });
    };
  });
});
