from django.utils import timezone

def is_challenge_active(challenge):
    if hasattr(challenge, 'contest_challenges') and challenge.contest_challenges.exists():
        contest = challenge.contest_challenges.first().contest
        now = timezone.now()
        return contest.start_time <= now <= contest.end_time
    return True 
 # No contest → always available
