document.addEventListener("DOMContentLoaded", function () {
  if (document.querySelector("#flw_btn")) {
    document.querySelector("#flw_btn").onclick = function () {
      const IdolID = this.dataset.idolid;
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
          IdolID: IdolID,
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
            if (data.flwed) {
              this.innerHTML = "Unfollow";
              document.querySelector("#n_flwers").innerHTML = data.n_flwer;
            } else {
              this.innerHTML = "Follow";
              document.querySelector("#n_flwers").innerHTML = data.n_flwer;
            }
          } else {
            alert("Action Failed!");
          }
        })
        .catch((error) => {
          console.log("Error: ", error);
        });
    };
  }
});
