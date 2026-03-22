import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('process')
def start(process): subprocess.run(['supervisorctl', 'start', process])
@cli.command()
@click.argument('process')
def stop(process): subprocess.run(['supervisorctl', 'stop', process])
@cli.command()
def status(): subprocess.run(['supervisorctl', 'status'])
@cli.command()
def reload(): subprocess.run(['supervisorctl', 'reload'])
if __name__ == '__main__': cli()
