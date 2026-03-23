import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glue running')
@cli.command()
def start(): click.echo('glue started')
if __name__ == '__main__': cli()
