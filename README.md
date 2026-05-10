

## Git Branching Strategy and Rules

- Main is main branch and considered true source of code for this project
- All code writting should be done so on feature branchs created from main
- Git Rule stops any direct pushes or force pushes to main
- Only way to get code onto main branch is to create a Pull Request from feature branch to the main branch.
    - Caveat - Since only me developing, have set the number of approvers to 0. This allows me to merge the PR's but forces the process at least. If more dev's join, increase to minimum of 1.