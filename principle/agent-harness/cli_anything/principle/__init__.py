import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('principle running')
@cli.command()
def start(): click.echo('principle started')
if __name__ == '__main__': cli()
