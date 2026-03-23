import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ibm running')
@cli.command()
def start(): click.echo('ibm started')
if __name__ == '__main__': cli()
