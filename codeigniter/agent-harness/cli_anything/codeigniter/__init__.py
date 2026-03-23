import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('codeigniter running')
@cli.command()
def start(): click.echo('codeigniter started')
if __name__ == '__main__': cli()
