import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wallpaper running')
@cli.command()
def start(): click.echo('wallpaper started')
if __name__ == '__main__': cli()
