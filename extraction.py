from lean_dojo import LeanGitRepo, trace

repo = LeanGitRepo(" https://github.com/SuhaibFarooqui-123/test_extraction", "944e8bfe8848416ad1c2bdbfd519c79b5ae90668")
trace(repo, dst_dir="traced_test_extraction")