from lean_dojo import LeanGitRepo, trace

# Try this only if you are 100% sure the repo is public
repo_url = "https://github.com/SuhaibFarooqui-123/test_extraction"
repo = LeanGitRepo(repo_url, "f0fd9d8035378033d0eb0b8779d86bb4175f7f2b")
trace(repo, dst_dir="traced_test_extraction")