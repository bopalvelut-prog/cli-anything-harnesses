import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('widely running')
@cli.command()
def start(): click.echo('widely started')
if __name__ == '__main__': cli()
