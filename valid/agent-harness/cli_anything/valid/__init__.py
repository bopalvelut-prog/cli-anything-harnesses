import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('valid running')
@cli.command()
def start(): click.echo('valid started')
if __name__ == '__main__': cli()
