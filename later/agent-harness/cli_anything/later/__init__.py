import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('later running')
@cli.command()
def start(): click.echo('later started')
if __name__ == '__main__': cli()
