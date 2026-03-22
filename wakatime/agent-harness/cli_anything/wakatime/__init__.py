import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def today(): click.echo('WakaTime today')
@cli.command()
def stats(): click.echo('WakaTime stats')
if __name__ == '__main__': cli()
