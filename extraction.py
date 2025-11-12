from lean_dojo import LeanGitRepo, trace

# Try this only if you are 100% sure the repo is public
repo_url = "https://github.com/SuhaibFarooqui-123/test_extraction"
repo = LeanGitRepo(repo_url, "ed0759441cd8a74d101df80a5615dfdf5a85961a")
trace(repo, dst_dir="traced_test_extraction")