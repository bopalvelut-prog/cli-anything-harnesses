import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('datafusion running')
@cli.command()
def start(): click.echo('datafusion started')
if __name__ == '__main__': cli()
