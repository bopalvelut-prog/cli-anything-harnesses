import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crazyflie running')
@cli.command()
def start(): click.echo('crazyflie started')
if __name__ == '__main__': cli()
