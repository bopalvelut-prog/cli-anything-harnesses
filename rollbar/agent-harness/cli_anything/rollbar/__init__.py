import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def deploy(): subprocess.run(['rollbar-cli', 'deploy'])
@cli.command()
def items(): click.echo('Rollbar items')
if __name__ == '__main__': cli()
