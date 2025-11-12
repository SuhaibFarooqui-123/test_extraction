from lean_dojo import LeanGitRepo, trace

repo = LeanGitRepo("https://github.com/SuhaibFarooqui-123/test_extraction.git", "ed0759441cd8a74d101df80a5615dfdf5a85961a")
trace(repo, dst_dir="traced_test_extraction")