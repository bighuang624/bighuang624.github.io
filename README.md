
<h1 align="center">
Homepage of Kyon Huang
</h1>

修改自 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io)，部署请参考官方[英文文档](https://github.com/RayeRen/acad-homepage.github.io)或[中文文档](https://github.com/RayeRen/acad-homepage.github.io/blob/main/docs/README-zh.md)。

额外做出的修改：

1. 参考[作者主页](https://github.com/RayeRen/rayeren.github.io)增加了每次更新主页时自动更新 Github Profile 的 action。相关文件包括 `.github\workflows\update_github_myprofile.yaml`、`github_myprofile_updater`，同时需要仓库页面的 Settings -> Secrets -> Actions -> New repository secret 中，添加 GHRS_GITHUB_API_TOKEN 变量，变量的值在 Github 账号的 Settings -> Developer Settings -> Fine-grained personal access tokens 里通过 Generate new token 获得，并且进行设置 Repository access: Only select repositories 并选择 Profile 对应仓库，Repository permissions 打开 Contents 修改权限。
2. 修改了 `_includes\fetch_google_scholar_stats.html` 来增加显示论文引用量的样式。现在可以通过 `<a class='paper_citations_badges' data='PAPER_ID' href="" target="_blank"></a>` 并修改 PAPER_ID 来自动生成 badge，而不是原模板只能通过文字显示引用量。