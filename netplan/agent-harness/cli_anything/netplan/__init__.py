import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('netplan running')
@cli.command()
def start(): click.echo('netplan started')
if __name__ == '__main__': cli()
