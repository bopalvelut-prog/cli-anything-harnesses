import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Emby status')
@cli.command()
def libraries(): click.echo('Media libraries')
if __name__ == '__main__': cli()
