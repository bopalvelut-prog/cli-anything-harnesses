import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ivy running')
@cli.command()
def start(): click.echo('ivy started')
if __name__ == '__main__': cli()
