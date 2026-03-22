import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def apps(): subprocess.run(['dokku', 'apps:list'])
@cli.command()
@click.argument('app')
def logs(app): subprocess.run(['dokku', 'logs', app])
@cli.command()
@click.argument('app')
def restart(app): subprocess.run(['dokku', 'ps:restart', app])
if __name__ == '__main__': cli()
