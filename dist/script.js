const form=document.getElementById("score"),formSubmit=t=>{t.preventDefault();const e=new FormData(t.target);axios.post("http://localhost:8000",{id:e.get("id")}).then((t=>{200==t.status&&console.log(t.data)}))};form.addEventListener("submit",formSubmit,!1);//# sourceMappingURL=script.js.map
