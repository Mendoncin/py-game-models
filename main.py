import init_django_orm  # noqa
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    for name, data in dados.items():

        race_data = data["race"]
        race = Race.objects.filter(name=race_data["name"]).first()

        if not race:
            race = Race(
                name=race_data["name"],
                description=race_data.get("description", "")
            )
            race.save()

        for skill_data in race_data.get("skills", []):
            skill = Skill.objects.filter(name=skill_data["name"]).first()

            if not skill:
                skill = Skill(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )
                skill.save()

        guild = None
        guild_data = data.get("guild")

        if guild_data:
            guild = Guild.objects.filter(name=guild_data["name"]).first()

            if not guild:
                guild = Guild(
                    name=guild_data["name"],
                    description=guild_data.get("description")
                )
                guild.save()

        player = Player.objects.filter(nickname=name).first()

        if not player:
            player = Player(
                nickname=name,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )
            player.save()


if __name__ == "__main__":
    main()
