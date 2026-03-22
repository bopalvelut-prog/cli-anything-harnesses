import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Lidarr status')
@cli.command()
def artists(): click.echo('Artists list')
if __name__ == '__main__': cli()
