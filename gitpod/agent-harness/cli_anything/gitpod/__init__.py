import click
@click.group()
def cli(): pass
@cli.command()
def open(): click.echo('Gitpod open')
@cli.command()
def status(): click.echo('Gitpod status')
if __name__ == '__main__': cli()
