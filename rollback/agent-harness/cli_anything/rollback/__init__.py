import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rollback running')
@cli.command()
def start(): click.echo('rollback started')
if __name__ == '__main__': cli()
