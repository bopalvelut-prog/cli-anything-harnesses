import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arsenal running')
@cli.command()
def start(): click.echo('arsenal started')
if __name__ == '__main__': cli()
