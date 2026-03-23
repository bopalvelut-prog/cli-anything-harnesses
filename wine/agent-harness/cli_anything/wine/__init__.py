import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wine running')
@cli.command()
def start(): click.echo('wine started')
if __name__ == '__main__': cli()
