import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('text running')
@cli.command()
def start(): click.echo('text started')
if __name__ == '__main__': cli()
