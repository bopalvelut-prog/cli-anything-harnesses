import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ipmitool running')
@cli.command()
def start(): click.echo('ipmitool started')
if __name__ == '__main__': cli()
