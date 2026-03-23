import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('operation running')
@cli.command()
def start(): click.echo('operation started')
if __name__ == '__main__': cli()
