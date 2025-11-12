from lean_dojo import LeanGitRepo, trace

# Try this only if you are 100% sure the repo is public
repo_url = "https://github.com/SuhaibFarooqui-123/test_extraction"
repo = LeanGitRepo(repo_url, "a50b089d7c417dbe718ccf53d0ca786ea849e1c3")
trace(repo, dst_dir="traced_test_extraction")