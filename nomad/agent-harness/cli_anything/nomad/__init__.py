import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['nomad', 'status'])
@cli.command()
@click.argument('job')
def run(job): subprocess.run(['nomad', 'run', job])
@cli.command()
@click.argument('job')
def stop(job): subprocess.run(['nomad', 'stop', job])
if __name__ == '__main__': cli()
