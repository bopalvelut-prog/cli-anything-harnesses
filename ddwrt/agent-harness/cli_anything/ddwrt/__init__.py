import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('DD-WRT running')
@cli.command()
def reboot(): click.echo('DD-WRT rebooting')
if __name__ == '__main__': cli()
