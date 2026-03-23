import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('seriously running')
@cli.command()
def start(): click.echo('seriously started')
if __name__ == '__main__': cli()
