import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Tautulli status')
@cli.command()
def history(): click.echo('Watch history')
if __name__ == '__main__': cli()
