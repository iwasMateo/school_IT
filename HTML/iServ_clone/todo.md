[] Make all the subsites functional
[] make them use this code:
    ´´´
        const div = document.querySelector("#myDiv");
        div.insertAdjacentHTML("afterbegin", `
        <p>New content</p>
    `);
    ´´´