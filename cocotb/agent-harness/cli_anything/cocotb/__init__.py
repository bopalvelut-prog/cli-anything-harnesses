import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cocotb running')
@cli.command()
def start(): click.echo('cocotb started')
if __name__ == '__main__': cli()
