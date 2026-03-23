import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('corner running')
@cli.command()
def start(): click.echo('corner started')
if __name__ == '__main__': cli()
