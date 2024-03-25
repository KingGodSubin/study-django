const moreButton = document.getElementById("more");
    let page = 1
    const getList = (callback) => {
        fetch(`http://127.0.0.1:8000/post/list/${page}`)
        // 서버로부터 응답을 받아주는 애 then
        // 화면이 서버랑 통신할 수 있고 서버가 DB랑 통신할 수 있음
        .then((response) => response.json())
        .then((posts) => {
            if(callback){
                callback(posts)
            }
        })
    }

    const showList = (post_info) => {
        if(!post_info.hasNext){
            moreButton.style.display = 'none'
        }
        let posts = post_info.posts
        const table = document.querySelector("table");
        posts.forEach((post) => {
            table.innerHTML += `
                <tr>
                    <td>${post.id}</td>
                    <td><a href="/post/detail/?id=${post.id}">${post.post_title}</a></td>
                    <td>${post.member_name}</td>
                    <td>${post.post_view_count}</td>
                </tr>
            `
        });
    }

    getList(showList);

    moreButton.addEventListener("click", (e) => {
        page ++;
        getList(showList);
    });